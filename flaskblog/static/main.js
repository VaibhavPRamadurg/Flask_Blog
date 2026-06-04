
document.addEventListener('DOMContentLoaded', () => {

    
    
    
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu    = document.getElementById('mobile-menu');

    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            const isOpen = !mobileMenu.classList.contains('hidden');
            mobileMenu.classList.toggle('hidden', isOpen);
            
            const icon = mobileMenuBtn.querySelector('svg path');
            if (icon) {
                icon.setAttribute('d', isOpen
                    ? 'M4 6h16M4 12h16M4 18h16'      
                    : 'M6 18L18 6M6 6l12 12'          
                );
            }
        });
    }

    
    
    
    const toasts = document.querySelectorAll('.flash-toast');
    toasts.forEach((toast) => {
        
        const closeBtn = toast.querySelector('.flash-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => dismissToast(toast));
        }

        
        setTimeout(() => dismissToast(toast), 4500);
    });

    function dismissToast(el) {
        el.classList.add('hiding');
        
        el.addEventListener('transitionend', () => el.remove(), { once: true });
    }

    
    
    
    const modal     = document.getElementById('deleteModal');
    const deleteBtn = document.getElementById('btn-delete-post');
    const closeBtns = document.querySelectorAll('[data-dismiss="modal"]');

    if (modal && deleteBtn) {
        const panel = modal.querySelector('.modal-panel');

        
        deleteBtn.addEventListener('click', openModal);

        
        closeBtns.forEach(btn => btn.addEventListener('click', closeModal));

        
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });

        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
                closeModal();
            }
        });

        function openModal() {
            modal.classList.remove('hidden');
            modal.classList.add('flex');
            
            requestAnimationFrame(() => requestAnimationFrame(() => {
                modal.classList.remove('opacity-0');
                if (panel) {
                    panel.classList.remove('scale-95', 'opacity-0');
                    panel.classList.add('scale-100', 'opacity-100');
                }
            }));
        }

        function closeModal() {
            modal.classList.add('opacity-0');
            if (panel) {
                panel.classList.remove('scale-100', 'opacity-100');
                panel.classList.add('scale-95', 'opacity-0');
            }
            setTimeout(() => {
                modal.classList.remove('flex');
                modal.classList.add('hidden');
            }, 280);
        }
    }

    
    
    
    const fileInput  = document.querySelector('input[type="file"]');
    const fileLabel  = document.getElementById('file-chosen');
    if (fileInput && fileLabel) {
        fileInput.addEventListener('change', function () {
            fileLabel.textContent = this.files[0]
                ? this.files[0].name
                : 'No file chosen';
        });
    }

    
    
    
    const header = document.querySelector('header');
    if (header) {
        const onScroll = () => {
            if (window.scrollY > 8) {
                header.classList.add('shadow-lg', 'shadow-black/40');
            } else {
                header.classList.remove('shadow-lg', 'shadow-black/40');
            }
        };
        window.addEventListener('scroll', onScroll, { passive: true });
    }

});
