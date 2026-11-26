from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
try:
    from xhtml2pdf import pisa
except ImportError:
    pisa = None

from .forms import CarrierInfoForm, BankingForm, TermsForm, SignForm
from .models import CarrierAgreement


def carrier_info(request):
    if request.method == 'POST':
        carrier_form = CarrierInfoForm(request.POST)
        banking_form = BankingForm(request.POST)
        if carrier_form.is_valid() and banking_form.is_valid():
            obj = carrier_form.save(commit=False)
            # merge banking form data into the same object
            obj.bank_name = banking_form.cleaned_data['bank_name']
            obj.account_number = banking_form.cleaned_data['account_number']
            obj.account_type = banking_form.cleaned_data['account_type']
            obj.save()

            request.session['agreement_id'] = obj.id
            messages.success(request, "✅ Carrier and Banking Information saved successfully.")
            return redirect('agreements:conditions')
        else:
            messages.warning(request, "⚠️ Please correct the errors below.")
    else:
        carrier_form = CarrierInfoForm()
        banking_form = BankingForm()

    return render(request, 'agreements/carrier_info.html', {
        'carrier_form': carrier_form,
        'banking_form': banking_form,
        'step': 1
    })


def conditions(request):
    agreement_id = request.session.get('agreement_id')
    if not agreement_id:
        messages.warning(request, "Please complete carrier information first.")
        return redirect('agreements:carrier_info')

    obj = get_object_or_404(CarrierAgreement, id=agreement_id)

    if request.method == 'POST':
        form = TermsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Terms and conditions accepted.")
            return redirect('agreements:sign')
        else:
            messages.error(request, "⚠️ Please accept the terms before continuing.")
    else:
        form = TermsForm(instance=obj)

    return render(request, 'agreements/conditions.html', {'form': form, 'step': 2, 'obj': obj})


def sign(request):
    agreement_id = request.session.get('agreement_id')
    if not agreement_id:
        messages.warning(request, "Please complete previous steps first.")
        return redirect('agreements:carrier_info')

    obj = get_object_or_404(CarrierAgreement, id=agreement_id)

    if request.method == 'POST':
        form = SignForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Agreement signed successfully.")
            return redirect('agreements:preview')
        else:
            messages.error(request, "⚠️ Please fill all required signature fields correctly.")
    else:
        form = SignForm(instance=obj)

    return render(request, 'agreements/sign.html', {'form': form, 'step': 3, 'obj': obj})


def preview(request):
    agreement_id = request.session.get('agreement_id')
    if not agreement_id:
        messages.warning(request, "Please complete the agreement first.")
        return redirect('agreements:carrier_info')

    obj = get_object_or_404(CarrierAgreement, id=agreement_id)

    if request.method == 'POST':
        messages.success(request, "✅ Agreement ready for final confirmation.")
        return redirect('agreements:done')

    return render(request, 'agreements/preview.html', {'obj': obj, 'step': 4})


def done(request):
    agreement_id = request.session.pop('agreement_id', None)
    obj = None
    if agreement_id:
        obj = get_object_or_404(CarrierAgreement, id=agreement_id)
        messages.success(request, "🎉 Agreement completed successfully. Thank you!")
    else:
        messages.warning(request, "Session expired or already completed.")
    return render(request, 'agreements/done.html', {'obj': obj, 'step': 5})


# ✅ Download Full Agreement PDF
def agreement_pdf(request, pk):
    obj = get_object_or_404(CarrierAgreement, pk=pk)
    template_path = 'agreements/agreement_pdf.html'
    context = {'obj': obj}
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Agreement_{obj.carrier_name}.pdf"'

    if pisa is None:
        messages.error(request, "xhtml2pdf library is not installed. Please run 'pip install xhtml2pdf'.")
        return redirect('agreements:done')

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        messages.error(request, "Error generating PDF. Please try again.")
        return redirect('agreements:done')

    messages.success(request, "📄 PDF downloaded successfully.")
    return response




def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def service1(request):
    return render(request, 'frontend/service-rented-trailer.html')


def service2(request):
    return render(request, 'frontend/service-twic.html')


def service3(request):
    return render(request, 'frontend/service-insurance.html')


def service4(request):
    return render(request, 'frontend/service-factoring.html')


def payments(request):
    return render(request, 'frontend/payment.html')